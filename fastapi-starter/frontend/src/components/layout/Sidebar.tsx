import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  BrainCircuit,
  Cpu,
  Film,
  Github,
  LayoutDashboard,
  MapPin,
  MessageSquare,
  Menu,
  X,
} from "lucide-react";
import { Link, useLocation } from "react-router-dom";

const navItems = [
  { name: "Dashboard", path: "/", icon: LayoutDashboard },
  { name: "Movies", path: "/movies", icon: Film },
  { name: "Comments", path: "/comments", icon: MessageSquare },
  { name: "Theaters", path: "/theaters", icon: MapPin },
  { name: "Sentiment ML", path: "/ml", icon: BrainCircuit },
];

export const Sidebar = () => {
  const location = useLocation();
  const [isMobileOpen, setIsMobileOpen] = useState(false);

  const sidebarContent = (
    <>
      <div className="flex gap-3 items-center px-2 mb-8">
        <div className="flex justify-center items-center w-9 h-9 rounded-lg border shadow-lg backdrop-blur-sm bg-white/10 border-slate-700/20 shrink-0">
          <Cpu className="text-white" size={18} />
        </div>
        <div className="min-w-0">
          <h2 className="text-sm font-bold tracking-tight text-white truncate">FastAPI</h2>
          <p className="text-[10px] font-semibold text-slate-400 tracking-wide uppercase truncate">
            Intelligence
          </p>
        </div>
      </div>

      <nav className="flex-1 space-y-1.5">
        {navItems.map((item) => {
          const isActive = location.pathname === item.path;
          const Icon = item.icon;

          return (
            <Link
              key={item.path}
              to={item.path}
              onClick={() => setIsMobileOpen(false)}
              className={`flex items-center gap-2.5 px-3 py-2.5 rounded-lg transition-all duration-200 group ${
                isActive
                  ? "bg-white/10 text-white border border-slate-600/30 shadow-lg backdrop-blur-sm rounded-lg"
                  : "text-slate-400 hover:text-white hover:bg-white/5 rounded-lg"
              }`}
            >
              <Icon
                size={16}
                className={`${isActive ? "text-white" : "text-slate-500 group-hover:text-white"} transition-colors shrink-0`}
              />
              <span className="text-sm font-medium tracking-tight truncate">{item.name}</span>
              {isActive && (
                <motion.div
                  layoutId="active-pill"
                  className="ml-auto w-1.5 h-1.5 rounded-full bg-white shrink-0"
                />
              )}
            </Link>
          );
        })}
      </nav>

      <a
        href="https://github.com/ragulpalanisamy/python-starter-kit"
        target="_blank"
        rel="noreferrer"
        className="flex items-center gap-2.5 px-3 py-2.5 text-slate-400 hover:text-white hover:bg-white/5 rounded-lg transition-colors text-xs font-semibold uppercase tracking-wide"
      >
        <Github size={14} />
        <span className="truncate">Github</span>
      </a>
    </>
  );

  return (
    <>
      {/* Mobile Menu Button */}
      <button
        onClick={() => setIsMobileOpen(!isMobileOpen)}
        className="fixed top-4 left-4 z-50 p-2 rounded-lg border shadow-lg backdrop-blur-xl transition-all lg:hidden bg-slate-900/90 border-slate-700/20 text-slate-300 hover:text-white hover:bg-slate-800/90 shadow-black/20"
        aria-label="Toggle menu"
      >
        {isMobileOpen ? <X size={20} /> : <Menu size={20} />}
      </button>

      {/* Mobile Overlay */}
      <AnimatePresence>
        {isMobileOpen && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setIsMobileOpen(false)}
            className="fixed inset-0 z-40 backdrop-blur-sm lg:hidden bg-black/50"
          />
        )}
      </AnimatePresence>

      {/* Desktop Sidebar - Always Visible */}
      <aside className="hidden sticky top-0 z-30 flex-col p-2 w-64 h-screen border-r backdrop-blur-2xl lg:flex bg-slate-950/80 border-slate-700/20 shrink-0">
        {sidebarContent}
      </aside>

      {/* Mobile Sidebar */}
      <AnimatePresence>
        {isMobileOpen && (
          <motion.aside
            initial={{ x: "-100%" }}
            animate={{ x: 0 }}
            exit={{ x: "-100%" }}
            transition={{ type: "spring", damping: 25, stiffness: 200 }}
            className="flex fixed top-0 left-0 z-50 flex-col p-2 w-64 h-screen border-r backdrop-blur-2xl lg:hidden bg-slate-950/95 border-slate-700/20"
          >
            {sidebarContent}
          </motion.aside>
        )}
      </AnimatePresence>
    </>
  );
};
