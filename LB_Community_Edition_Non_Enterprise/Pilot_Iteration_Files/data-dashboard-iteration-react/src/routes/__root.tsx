import type { QueryClient } from "@tanstack/react-query";
import { createRootRouteWithContext, Outlet } from "@tanstack/react-router";
import { TanStackRouterDevtools } from "@tanstack/react-router-devtools";
import TanStackQueryLayout from "../integrations/tanstack-query/layout.tsx";

interface AuthenticatedRouteContext {
	queryClient: QueryClient;
}

export const Route = createRootRouteWithContext<AuthenticatedRouteContext>()({
	component: () => (
		<>
			<Outlet />
			<TanStackRouterDevtools />
			<TanStackQueryLayout />
		</>
	),
});
