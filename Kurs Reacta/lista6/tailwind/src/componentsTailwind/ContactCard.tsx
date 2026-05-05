function ContactCard({
  email,
  github,
  linkedin,
}: {
  email: string
  github: string
  linkedin: string
}) {
  return (
    <div className="rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <h3 className="m-0 mb-2.5 text-xs font-bold tracking-[0.1em] text-slate-500 uppercase dark:text-slate-500 midnight:text-violet-500">
        Contact
      </h3>
      <div className="flex flex-col gap-1.5">
        <p className="m-0 text-[0.88rem]">
          <span className="mr-1.5 font-semibold text-slate-900 dark:text-slate-200 midnight:text-violet-300">
            Email
          </span>
          {email}
        </p>
        <p className="m-0 text-[0.88rem]">
          <span className="mr-1.5 font-semibold text-slate-900 dark:text-slate-200 midnight:text-violet-300">
            GitHub
          </span>
          {github}
        </p>
        <p className="m-0 text-[0.88rem]">
          <span className="mr-1.5 font-semibold text-slate-900 dark:text-slate-200 midnight:text-violet-300">
            LinkedIn
          </span>
          {linkedin}
        </p>
      </div>
    </div>
  )
}

export default ContactCard
