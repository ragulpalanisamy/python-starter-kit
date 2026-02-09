import { createContext } from "react";

interface AppContextType {
  theme: "light" | "dark";
  toggleTheme: () => void;
}

export const AppContext = createContext<AppContextType | undefined>(undefined);
