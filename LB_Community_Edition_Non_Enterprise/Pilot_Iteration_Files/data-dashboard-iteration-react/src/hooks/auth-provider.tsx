
const queryClient = new QueryClient();

export function getContext() {
	return {
		queryClient,
	};
}

export function Provider({ children }: { children: React.ReactNode }) {
	return (
		<AuthProvider client={queryClient}>{children}</AuthProvider>
	);
}
