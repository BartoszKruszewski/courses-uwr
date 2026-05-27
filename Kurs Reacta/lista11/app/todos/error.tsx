"use client";

export default function Error({
  error,
  reset,
}: {
  error: Error & { digest?: string }
  reset: () => void
}) {
  return (
    <div className="flex flex-col items-center justify-center py-12 px-4 text-center">
      <div className="bg-red-50 text-red-800 border border-red-200 rounded-lg p-6 max-w-md w-full">
        <h2 className="text-xl font-bold mb-2">Something went wrong!</h2>
        <p className="text-red-600 mb-6">{error.message}</p>
        <button 
          onClick={() => reset()}
          className="inline-flex justify-center rounded-md bg-red-600 px-4 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-600 transition-colors"
        >
          Try again
        </button>
      </div>
    </div>
  )
}
