import React from "react";
import { Box, Button, Typography, Container } from "@mui/material";
import { useNavigate } from "react-router-dom";

const LandingPage: React.FC = () => {
  const navigate = useNavigate();

  return (
    <Container maxWidth="md" sx={{ textAlign: "center", mt: 8 }}>
      <Typography variant="h2" component="h1" gutterBottom>
        GenAI Haircut Tracker
      </Typography>
      <Typography variant="h5" color="text.secondary" gutterBottom>
        Keep track of your haircuts, get AI feedback, and find the best barbers.
      </Typography>

      <Box mt={4}>
        <Button
          variant="contained"
          color="primary"
          size="large"
          sx={{ mr: 2 }}
          onClick={() => navigate("/upload")}
        >
          Upload Your Haircut
        </Button>
        <Button
          variant="outlined"
          color="secondary"
          size="large"
          onClick={() => navigate("/profile")}
        >
          View Your History
        </Button>
        <Button
          variant="outlined"
          color="secondary"
          size="large"
          sx={{ ml: 2 }}
          onClick={() => navigate("/analyze")}
        >
          Ask the AI
        </Button>
      </Box>

      <Box mt={6}>
        <img
          src="/haircut-illustration.png"
          alt="Haircut illustration"
          style={{ maxWidth: "100%" }}
        />
      </Box>
    </Container>
  );
};

export default LandingPage;
