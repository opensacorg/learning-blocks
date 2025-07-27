export default function AppH5A({ children }: { children: React.ReactNode }) {
	return (
		<div className="min-h-screen bg-gray-100">
						<Navbar />
			{children}
		</div>
	)
}