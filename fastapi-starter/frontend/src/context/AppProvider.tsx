import React, { useState } from "react";
import type { ReactNode } from "react";
import { AppContext } from "./AppContext";

export const AppProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [theme, setTheme] = useState<"light" | "dark">("dark");

  const toggleTheme = () => {
    setTheme((prev) => (prev === "light" ? "dark" : "light"));
  };

  return <AppContext.Provider value={{ theme, toggleTheme }}>{children}</AppContext.Provider>;
};
