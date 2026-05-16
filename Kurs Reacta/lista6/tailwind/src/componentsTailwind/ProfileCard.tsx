function ProfileCard({
  name,
  title,
  location,
  avatar,
}: {
  name: string
  title: string
  location: string
  avatar: string
}) {
  return (
    <div className="flex items-center gap-5 rounded-xl border border-slate-200 bg-white p-6 dark:border-slate-700 dark:bg-slate-800 midnight:border-[#3b2756] midnight:bg-[#261838]">
      <div className="flex h-[72px] w-[72px] shrink-0 items-center justify-center rounded-full bg-blue-500 text-[1.4rem] font-bold text-white dark:bg-indigo-500 midnight:bg-violet-600">
        {avatar}
      </div>
      <div>
        <h2 className="m-0 text-[1.3rem] font-bold text-slate-900 dark:text-slate-100 midnight:text-violet-100">
          {name}
        </h2>
        <p className="mt-1 mb-0 text-sm font-medium opacity-75">{title}</p>
        <p className="mt-1 mb-0 text-[0.8rem] opacity-60">{location}</p>
      </div>
    </div>
  )
}

export default ProfileCard
