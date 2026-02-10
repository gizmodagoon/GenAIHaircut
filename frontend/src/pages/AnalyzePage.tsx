import React, { useState } from "react";
import {
  Container,
  Typography,
  TextField,
  Button,
  CircularProgress,
  Alert,
  Box,
  Divider,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import ReactMarkdown from "react-markdown";
import api from "../api";

const AnalyzePage: React.FC = () => {
  const navigate = useNavigate();
  const [prompt, setPrompt] = useState("");
  const [analysis, setAnalysis] = useState<any>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = () => {
    if (!prompt.trim()) return;
    setLoading(true);
    setError(null);
    setAnalysis(null);
    api
      .post<{ analysis: any }>("/haircuts/analyze", { prompt })
      .then((res) => setAnalysis(res.data.analysis.message.content))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  };

  return (
    <Container sx={{ mt: 8 }}>
      <Button
        variant="outlined"
        color="primary"
        onClick={() => navigate("/")}
        sx={{ mb: 2 }}
      >
        Back to Home
      </Button>
      <Typography variant="h4" gutterBottom>
        Ask the AI
      </Typography>

      <Box sx={{ display: "flex", gap: 2, mb: 3 }}>
        <TextField
          label="Ask a haircut question"
          variant="outlined"
          fullWidth
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter" && !loading) handleSubmit();
          }}
        />
        <Button
          variant="contained"
          color="primary"
          onClick={handleSubmit}
          disabled={loading || !prompt.trim()}
        >
          Submit
        </Button>
      </Box>

      {loading && <CircularProgress />}
      {error && <Alert severity="error">{error}</Alert>}
      {analysis && (
        <Box sx={{ mt: 2 }}>
          <Typography variant="h6" gutterBottom>
            AI Response
          </Typography>
          <Divider sx={{ mb: 2 }} />
          {analysis.map((item: any, index: number) => (
            <ReactMarkdown key={index}>{item.text}</ReactMarkdown>
          ))}
          
        </Box>
      )}
    </Container>
  );
};

export default AnalyzePage;
