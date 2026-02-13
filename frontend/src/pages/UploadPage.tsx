import React from "react";
import { Button, Container, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom"

const UploadPage: React.FC = () => {
  const navigate = useNavigate();
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
        Upload Your Haircut
      </Typography>
      <Typography>
        (Upload feature coming soon – this is a placeholder page.)
      </Typography>
    </Container>
  );
};

export default UploadPage;
