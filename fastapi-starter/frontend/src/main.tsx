import { HeroUIProvider } from "@heroui/react";
import { Toaster } from "react-hot-toast";
import { Provider } from "react-redux";
import { Analytics } from "@vercel/analytics/react";
import { SpeedInsights } from "@vercel/speed-insights/react";
import { store } from "./store";
import App from "./App";
import "./index.css";
import React from "react";
import ReactDOM from "react-dom/client";

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <Provider store={store}>
      <HeroUIProvider>
        <div className="dark text-foreground bg-background min-h-screen">
          <App />
          <Toaster position="bottom-right" reverseOrder={false} />
        </div>
      </HeroUIProvider>
    </Provider>
    <Analytics />
    <SpeedInsights />
  </React.StrictMode>
);
