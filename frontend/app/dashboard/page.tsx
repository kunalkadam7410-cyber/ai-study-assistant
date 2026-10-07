const apiUrl = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

async function getDashboardStats() {
  const res = await fetch(`${apiUrl}/api/dashboard/1`);
  const data = await res.json();
  return data;
}

export default async function HomePage() {
  const stats = await getDashboardStats().catch(() => ({
    materials_count: 0,
    flashcards_count: 0,
    quiz_count: 0,
  }));

  return (
    <main className="min-h-screen p-8">
      <div className="mx-auto max-w-6xl">
        <header className="mb-10 flex items-center justify-between rounded-2xl bg-white p-6 shadow-soft">
          <div>
            <p className="text-sm font-medium uppercase tracking-[0.2em] text-primary-600">AI Study Assistant</p>
            <h1 className="mt-2 text-3xl font-bold">Study smarter with AI</h1>
          </div>
          <a href="/dashboard" className="rounded-xl bg-primary-600 px-5 py-3 font-medium text-white shadow-sm hover:bg-primary-700">
            Open dashboard
          </a>
        </header>

        <section className="grid gap-6 md:grid-cols-3">
          <StatCard title="Materials" value={stats.materials_count} description="Uploaded notes and files" />
          <StatCard title="Flashcards" value={stats.flashcards_count} description="Active study cards" />
          <StatCard title="Quizzes" value={stats.quiz_count} description="Generated practice tests" />
        </section>

        <section className="mt-10 grid gap-6 lg:grid-cols-2">
          <div className="rounded-2xl bg-white p-6 shadow-soft">
            <h2 className="mb-4 text-xl font-semibold">Why students use it</h2>
            <ul className="space-y-3 text-slate-700">
              <li>• Ask questions about your notes and get clear explanations.</li>
              <li>• Turn big study material into concise flashcards.</li>
              <li>• Generate quiz questions to self-test before exams.</li>
              <li>• Track which subjects you are studying most.</li>
            </ul>
          </div>

          <div className="rounded-2xl bg-white p-6 shadow-soft">
            <h2 className="mb-4 text-xl font-semibold">Workflow</h2>
            <ol className="space-y-3 text-slate-700">
              <li>1. Upload notes or PDF documents.</li>
              <li>2. Ask a question or generate a summary.</li>
              <li>3. Create flashcards and quizzes from your material.</li>
              <li>4. Review progress and revise key concepts.</li>
            </ol>
          </div>
        </section>
      </div>
    </main>
  );
}

function StatCard({ title, value, description }: { title: string; value: number; description: string }) {
  return (
    <div className="rounded-2xl bg-white p-6 shadow-soft">
      <p className="text-sm uppercase tracking-[0.2em] text-slate-500">{title}</p>
      <p className="mt-4 text-4xl font-bold text-primary-600">{value}</p>
      <p className="mt-2 text-sm text-slate-600">{description}</p>
    </div>
  );
}
