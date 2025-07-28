import { createFileRoute } from "@tanstack/react-router";
import GaugeChart from "../../integrations/apache-echarts/GaugeChart";
import "../../integrations/apache-echarts/gauge-chart.css";
import { useQuery } from "@tanstack/react-query";

export const Route = createFileRoute("/_home/")({
	component: App,
});

function App() {
	const { data: gaugeData } = useQuery({
		// Using the "test" query key as you requested
		queryKey: ["test"],
		// Mocking a query function that returns data for the gauge
		queryFn: () => Promise.resolve({ value: 0.8, name: "Test Rating" }),
		// Providing initial data for immediate rendering
		initialData: { value: 0.8, name: "Initial Rating" },
	});

	return (
		<div className="bg-[#282c34] min-h-screen text-white text-[calc(10px+2vmin)]">
				<p>
					Edit <code>src/routes/index.tsx</code> and save to reload.
				</p>
				<GaugeChart />
				<a
					className="text-[#61dafb] hover:underline"
					href="https://reactjs.org"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn React
				</a>
				<a
					className="text-[#61dafb] hover:underline"
					href="https://tanstack.com"
					target="_blank"
					rel="noopener noreferrer"
				>
					Learn TanStack
				</a>
		</div>
	);
}
