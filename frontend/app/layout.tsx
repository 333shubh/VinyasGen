import type { Metadata } from "next";

import "maplibre-gl/dist/maplibre-gl.css";
import "maplibre-gl-draw/dist/mapbox-gl-draw.css";
import "./globals.css";

export const metadata: Metadata = {
  title: "VinyasGen",
  description: "Generative intelligence for urban regeneration",
  icons: {
    icon: "/favicon.svg"
  }
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
