import React, {
  useState,
  useRef, 
  useEffect
} from "react";
import {
  Button,
  Container,
  Typography,
  TextField,
  IconButton,
  CircularProgress,
  Alert,
  Box,
  Paper,
} from "@mui/material";
import SendIcon from "@mui/icons-material/Send";
import ArrowBackIcon from "@mui/icons-material/ArrowBack";
import RefreshIcon from "@mui/icons-material/Refresh";
import { useNavigate } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import api from "../api";

interface Message {
  role: "user" | "assistant";
  content: string;
}

const ChatWithAIPage: React.FC = () => {
  const navigate = useNavigate();
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState<Message[]>([]);
  const [messagesLoading, setMessagesLoading] = useState(false);
  const [messagesError, setMessagesError] = useState<string | null>(null);
  const [sessionLoading, setSessionLoading] = useState(false);
  const [sessionError, setSessionError] = useState<string | null>(null);
  const messagesEndRef = useRef<HTMLDivElement>(null);
  const sessionIdRef = useRef<string | null>(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  useEffect(() => {
    setSessionLoading(true);
    setSessionError(null);
    getChatSession();
    
    return () => {
      if(sessionIdRef.current){
        api.delete(`/barbers/chat-sessions/${sessionIdRef.current}`);
      }
    }
  }, []);

  const getChatSession = () => {
    setSessionLoading(true);
    setSessionError(null);

    api.post("/barbers/chat-sessions")
      .then((res) =>{
        sessionIdRef.current = res.data.session_id;
      })
      .catch((err) => setSessionError(err.message))
      .finally(() => setSessionLoading(false))
  }

  const handleSend = () => {
    const prompt = input.trim();
    if (!prompt || messagesLoading) return;

    const userMessage: Message = { role: "user", content: prompt };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setMessagesLoading(true);
    setMessagesError(null);

    api
      .post<{ response: string }>(`/barbers/chat-sessions/${sessionIdRef.current}/messages`, { prompt })
      .then((res) => {
        setMessages((prev) => [
          ...prev,
          { role: "assistant", content: res.data.response },
        ]);
      })
      .catch((err) => setMessagesError(err.message))
      .finally(() => setMessagesLoading(false));
  };

  return (
    <Container
      maxWidth="md"
      sx={{
        height: "100vh",
        display: "flex",
        flexDirection: "column",
        py: 2,
      }}
    >
      {/* Header */}
      <Box sx={{ display: "flex", alignItems: "center", gap: 1, mb: 2 }}>
        <IconButton onClick={() => navigate("/")} size="small">
          <ArrowBackIcon />
        </IconButton>
        <Typography variant="h5">Ask the AI Barber</Typography>
      </Box>

      {sessionLoading && (
        <Box sx={{
          display: 'flex',
          alignItems: "center",
          justifyContent: "center",
          flex: 1,
        }}>
          <CircularProgress />
        </Box>
      )}

      {sessionError && (
        <Alert
          severity="error"
          action={
            <Button color="inherit" size="small" startIcon={<RefreshIcon />} onClick={() => getChatSession()}>
              Retry
            </Button>
          }
        >
          {sessionError}
        </Alert>
      )}

      {!sessionLoading && sessionIdRef.current && (
        <>
          {/* Messages */}
          <Box
            sx={{
              flex: 1,
              overflowY: "auto",
              display: "flex",
              flexDirection: "column",
              gap: 2,
              pb: 2,
            }}
          >
            {messages.length === 0 && !messagesLoading && (
              <Box
                sx={{
                  flex: 1,
                  display: "flex",
                  alignItems: "center",
                  justifyContent: "center",
                }}
              >
                <Typography color="text.secondary">
                  Ask me anything about haircuts or hair care!
                </Typography>
              </Box>
            )}

            {messages.map((msg, i) => (
              <Box
                key={i}
                sx={{
                  display: "flex",
                  justifyContent: msg.role === "user" ? "flex-end" : "flex-start",
                }}
              >
                <Paper
                  elevation={1}
                  sx={{
                    px: 2,
                    py: 1.5,
                    maxWidth: "75%",
                    bgcolor: msg.role === "user" ? "primary.main" : "grey.100",
                    color:
                      msg.role === "user" ? "primary.contrastText" : "text.primary",
                    borderRadius: 2,
                    "& p": { m: 0 },
                  }}
                >
                  {msg.role === "assistant" ? (
                    <ReactMarkdown>{msg.content}</ReactMarkdown>
                  ) : (
                    <Typography>{msg.content}</Typography>
                  )}
                </Paper>
              </Box>
            ))}

            {messagesLoading && (
              <Box sx={{ display: "flex", justifyContent: "flex-start" }}>
                <CircularProgress size={24} />
              </Box>
            )}

            {messagesError && <Alert severity="error">{messagesError}</Alert>}
            <div ref={messagesEndRef} />
          </Box>

          {/* Input */}
          <Box
            sx={{ display: "flex", gap: 1, pt: 1, borderTop: 1, borderColor: "divider" }}
          >
            <TextField
              fullWidth
              size="small"
              placeholder="Type your question..."
              value={input}
              disabled={messagesLoading}
              onChange={(e) => setInput(e.target.value)}
              onKeyDown={(e) => {
                if (e.key === "Enter" && !e.shiftKey) {
                  e.preventDefault();
                  handleSend();
                }
              }}
            />
            <IconButton
              color="primary"
              onClick={handleSend}
              disabled={messagesLoading || !input.trim()}
            >
              <SendIcon />
            </IconButton>
          </Box>
        </>
      )}
    </Container>
  );
};

export default ChatWithAIPage;
