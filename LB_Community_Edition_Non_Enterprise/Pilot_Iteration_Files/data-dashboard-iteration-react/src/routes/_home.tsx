import { createFileRoute, Outlet } from "@tanstack/react-router";
import Navbar from "@/components/navbar-light/Navbar";

export const Route = createFileRoute("/_home")({
	component: HomeLayout,
});

export default function HomeLayout() {
	return (
		<>
			<Navbar />
			<Outlet />
		</>
	);
}
