"use client";

import { useFormStatus } from "react-dom";

export function TodoForm({
  action,
  initialData,
}: {
  action: (formData: FormData) => void;
  initialData?: { text: string; done: boolean };
}) {
  return (
    <form action={action} className="space-y-6 max-w-lg mt-6 mx-auto bg-gray-50 p-6 rounded-lg border border-gray-200">
      <FormFields initialData={initialData} />
    </form>
  );
}

function FormFields({ initialData }: { initialData?: { text: string; done: boolean } }) {
  const { pending } = useFormStatus();

  return (
    <>
      <div>
        <label htmlFor="text" className="block text-sm font-medium leading-6 text-gray-900 mb-1">
          Title
        </label>
        <div className="mt-2">
          <input
            id="text"
            name="text"
            type="text"
            defaultValue={initialData?.text}
            disabled={pending}
            required
            className="block w-full rounded-md border-0 py-2 px-3 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 placeholder:text-gray-400 focus:ring-2 focus:ring-inset focus:ring-blue-600 sm:text-sm sm:leading-6 disabled:opacity-50 disabled:bg-gray-100"
            placeholder="What needs to be done?"
          />
        </div>
      </div>

      {initialData !== undefined && (
        <div className="flex items-center gap-x-3 pt-2">
          <input
            id="done"
            name="done"
            type="checkbox"
            defaultChecked={initialData?.done}
            disabled={pending}
            className="h-5 w-5 rounded border-gray-300 text-blue-600 focus:ring-blue-600 disabled:opacity-50"
          />
          <label htmlFor="done" className="block text-sm font-medium leading-6 text-gray-900 cursor-pointer">
            Mark as Completed
          </label>
        </div>
      )}

      <div className="pt-4 border-t border-gray-200">
        <button
          type="submit"
          disabled={pending}
          className="inline-flex w-full justify-center rounded-md bg-blue-600 px-3 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-blue-700 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600 disabled:opacity-50 transition-colors"
        >
          {pending ? "Saving..." : "Save Todo"}
        </button>
      </div>
    </>
  );
}
