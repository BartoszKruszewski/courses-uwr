export default function Loading() {
  return (
    <div className="flex flex-col items-center justify-center py-12">
      <div className="w-8 h-8 border-4 border-blue-600 border-t-transparent rounded-full animate-spin mb-4"></div>
      <p className="text-lg font-medium text-gray-700">Loading data...</p>
    </div>
  );
}
