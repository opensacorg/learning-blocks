import { createFileRoute, Outlet } from "@tanstack/react-router";
import AppH5A from "@/components/layout/AppH5A";
import { useAuth } from "@/auth";

export const Route = createFileRoute("/_home")({
	component: HomeLayout,
});

export default function HomeLayout() {
	return (
		<AppH5A>
			<Outlet />
		</AppH5A>
	);
}
