export const PAGE_SIZES = {
  MOVIES: 10,
  COMMENTS: 12,
  THEATERS: 12,
  EMBEDDED_MOVIES: 9,
  DASHBOARD_MOVIES: 5,
} as const;

export const ROUTES = {
  DASHBOARD: "/",
  MOVIES: "/movies",
  COMMENTS: "/comments",
  THEATERS: "/theaters",
  ML: "/ml",
  SEMANTIC_SEARCH: "/semantic-search",
} as const;

export const NAV_ITEMS = [
  { name: "Dashboard", path: ROUTES.DASHBOARD, icon: "LayoutDashboard" },
  { name: "Movies", path: ROUTES.MOVIES, icon: "Film" },
  { name: "Comments", path: ROUTES.COMMENTS, icon: "MessageSquare" },
  { name: "Theaters", path: ROUTES.THEATERS, icon: "MapPin" },
  { name: "Sentiment ML", path: ROUTES.ML, icon: "BrainCircuit" },
  { name: "Semantic Search", path: ROUTES.SEMANTIC_SEARCH, icon: "Search" },
] as const;
