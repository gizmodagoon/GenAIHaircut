import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import LandingPage from "../pages/LandingPage";
import UploadPage from "../pages/UploadPage";
import ProfilePage from "../pages/ProfilePage";
import AnalyzePage from "../pages/AnalyzePage";

const AppRoutes: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<LandingPage />} />
        <Route path="/upload" element={<UploadPage />} />
        <Route path="/profile" element={<ProfilePage />} />
        <Route path="/analyze" element={<AnalyzePage />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;
