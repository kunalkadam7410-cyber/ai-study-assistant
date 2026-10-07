import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'AI Study Assistant',
  description: 'Upload notes and study smarter with AI',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
