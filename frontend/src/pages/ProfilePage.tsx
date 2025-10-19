import React from "react";
import { Container, Typography } from "@mui/material";

const ProfilePage: React.FC = () => {
  return (
    <Container sx={{ mt: 8 }}>
      <Typography variant="h4" gutterBottom>
        Your Haircut History
      </Typography>
      <Typography>
        (Profile/history view coming soon – this is a placeholder page.)
      </Typography>
    </Container>
  );
};

export default ProfilePage;
