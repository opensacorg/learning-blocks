import { Link } from "@tanstack/react-router";

export default function Navbar() {
	return (
		<div
			className="h-[4.25rem] bg-gray-200 text-gray-900 w-full
		shadow-[0_35px_60px_-15px_rgba(0,0,0,0.3)]
		"
		>
			<nav className="h-full flex items-center max-w-[82.5rem] mx-auto px-6 gap-2 justify-between">
				<div className="flex items-center h-full py-2">
					<Link
						className="pr-8 h-full rounded font-bold gap-[13px] text-[#013148] flex items-center leading-none tracking-wide"
						to="/"
					>
						<img src="/logo.svg" alt="Logo" className="h-10" />
						<span className="">
							Learning
							<br />
							Blocks
						</span>
					</Link>
					<Link
						to="/"
						className="pr-3 font-medium text-gray-500 rounded hover:text-gray-900  dark:text-gray-400 dark:hover:text-white py-1"
					>
						Get Started
					</Link>
					<div className="">
						<Link to="/" className="px-3 py-1 font-medium tracking-wide">
							Dashboard
						</Link>
					</div>
				</div>
				<Link to="/" className="font-medium">
					Home
				</Link>

				<div className="flex flex-row hidden">
					<div className="px-2 font-bold">
						<Link to="/">Home</Link>
					</div>

					<div className="px-2 font-bold">
						<Link to="/demo/tanstack-query">TanStack Query</Link>
					</div>

					<div className="px-2 font-bold">
						<Link to="/demo/form/simple">Simple Form</Link>
					</div>

					<div className="px-2 font-bold">
						<Link to="/demo/form/address">Address Form</Link>
					</div>

					<div className="px-2 font-bold">
						<Link to="/demo/table">TanStack Table</Link>
					</div>
				</div>
			</nav>
		</div>
	);
}
