function AboutCard({ text }: { text: string }) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <h3 className="m-0 mb-2.5 text-xs font-bold tracking-[0.1em] text-slate-500 uppercase dark:text-slate-500 midnight:text-violet-500">
        About
      </h3>
      <p className="m-0 text-[0.9rem] leading-[1.65]">{text}</p>
    </div>
  )
}

export default AboutCard
