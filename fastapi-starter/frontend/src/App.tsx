import { BrowserRouter, Route, Routes } from "react-router-dom";
import { MainLayout } from "./components/layout/MainLayout";
import { AppProvider } from "./context/AppProvider";
import { CommentsPage } from "./pages/Comments/CommentsPage";
import { DashboardPage } from "./pages/Dashboard/DashboardPage";
import { MLPage } from "./pages/ML/MLPage";
import { MoviesPage } from "./pages/Movies/MoviesPage";
import { TheatersPage } from "./pages/Theaters/TheatersPage";

function AppContent() {
  return (
    <>
      <Routes>
        <Route path="/" element={<DashboardPage />} />
        <Route path="/movies" element={<MoviesPage />} />
        <Route path="/comments" element={<CommentsPage />} />
        <Route path="/theaters" element={<TheatersPage />} />
        <Route path="/ml" element={<MLPage />} />
      </Routes>

      <footer className="mt-2 pt-2 border-t border-white/5 flex flex-col sm:flex-row justify-between items-center gap-2 text-[9px] font-semibold uppercase tracking-wide text-slate-500">
        <p>© 2026 FastAPI Starter Project</p>
        <div className="flex gap-2">
          <a href="#" className="hover:text-blue-500 transition-colors cursor-pointer">
            Documentation
          </a>
          <a href="#" className="hover:text-blue-500 transition-colors cursor-pointer">
            API Status
          </a>
          <a href="#" className="hover:text-blue-500 transition-colors cursor-pointer">
            Security
          </a>
        </div>
      </footer>
    </>
  );
}

function App() {
  return (
    <AppProvider>
      <BrowserRouter>
        <MainLayout>
          <AppContent />
        </MainLayout>
      </BrowserRouter>
    </AppProvider>
  );
}

export default App;
