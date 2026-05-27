export function TodoBadge({ done }: { done: boolean }) {
  if (done) {
    return (
      <span className="inline-flex items-center rounded-md bg-green-50 px-2 py-1 text-xs sm:text-sm font-medium text-green-700 ring-1 ring-inset ring-green-600/20">
        Completed
      </span>
    );
  }
  return (
    <span className="inline-flex items-center rounded-md bg-yellow-50 px-2 py-1 text-xs sm:text-sm font-medium text-yellow-800 ring-1 ring-inset ring-yellow-600/20">
      Active
    </span>
  );
}
