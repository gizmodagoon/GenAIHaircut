import React, { useEffect, useState } from "react";
import {
  Container,
  Typography,
  List,
  ListItem,
  ListItemText,
  CircularProgress,
  Alert,
  Button,
} from "@mui/material";
import { useNavigate } from "react-router-dom";
import api from "../api";

interface Haircut {
  id: number;
  style: string;
}

const ProfilePage: React.FC = () => {
  const navigate = useNavigate();
  const [haircuts, setHaircuts] = useState<Haircut[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    api
      .get<Haircut[]>("/haircuts")
      .then((res) => setHaircuts(res.data))
      .catch((err) => setError(err.message))
      .finally(() => setLoading(false));
  }, []);

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
        Your Haircut History
      </Typography>

      {loading && <CircularProgress />}
      {error && <Alert severity="error">Failed to load haircuts: {error}</Alert>}

      {!loading && !error && haircuts.length === 0 && (
        <Typography color="text.secondary">No haircuts found.</Typography>
      )}

      <List>
        {haircuts.map((haircut) => (
          <ListItem key={haircut.id} divider>
            <ListItemText
              primary={haircut.style}
              secondary={`ID: ${haircut.id}`}
            />
          </ListItem>
        ))}
      </List>
    </Container>
  );
};

export default ProfilePage;
