import { Link } from "@tanstack/react-router";
import DistrictSelector from "../district-selector/DistrictSelector";
import SearchBar from "../SearchBar";

export default function Navbar() {
	return (
		<div
			className="h-[4.25rem] bg-gray-200 text-gray-900 w-full
		shadow-[0_35px_60px_-15px_rgba(0,0,0,0.3)]
		"
		>
			<nav className="h-full flex items-center max-w-[82.5rem] mx-auto px-6 gap-2">
				<div className="flex items-center h-full py-2">
					<Link
						className="pr-4 h-full rounded font-bold gap-[13px] text-[#013148] flex items-center leading-none tracking-wide"
						to="/"
					>
						<img src="/logo.svg" alt="Logo" className="h-10"/>
						<span className="">
							Learning
							<br />
							Blocks
						</span>
					</Link>
					<DistrictSelector />
				</div>
				<div className="grow h-full flex items-center justify-end ">
					<SearchBar className="grow-1 hidden lg:block" />
					<Link to="/" className="lg:hidden">
						<img
							src="/icon/search.svg"
							alt="Search for information about a disctrict, school, or topic."
						/>
					</Link>
				</div>

				<div className="flex gap-4 ml-4">
					<Link to="/demo/table">
						<svg
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
						>
							<title>Accessibility options</title>
							<path
								d="M12 8C12.2761 8 12.5 7.77614 12.5 7.5C12.5 7.22386 12.2761 7 12 7C11.7239 7 11.5 7.22386 11.5 7.5C11.5 7.77614 11.7239 8 12 8Z"
								fill="currentColor"
							/>
							<path
								d="M10 16.5L12 13.5M12 13.5L14 16.5M12 13.5V11.5M12 11.5L15 10.5M12 11.5L9 10.5M3 12C3 13.1819 3.23279 14.3522 3.68508 15.4442C4.13738 16.5361 4.80031 17.5282 5.63604 18.364C6.47177 19.1997 7.46392 19.8626 8.55585 20.3149C9.64778 20.7672 10.8181 21 12 21C13.1819 21 14.3522 20.7672 15.4442 20.3149C16.5361 19.8626 17.5282 19.1997 18.364 18.364C19.1997 17.5282 19.8626 16.5361 20.3149 15.4442C20.7672 14.3522 21 13.1819 21 12C21 10.8181 20.7672 9.64778 20.3149 8.55585C19.8626 7.46392 19.1997 6.47177 18.364 5.63604C17.5282 4.80031 16.5361 4.13738 15.4442 3.68508C14.3522 3.23279 13.1819 3 12 3C10.8181 3 9.64778 3.23279 8.55585 3.68508C7.46392 4.13738 6.47177 4.80031 5.63604 5.63604C4.80031 6.47177 4.13738 7.46392 3.68508 8.55585C3.23279 9.64778 3 10.8181 3 12ZM12.5 7.5C12.5 7.77614 12.2761 8 12 8C11.7239 8 11.5 7.77614 11.5 7.5C11.5 7.22386 11.7239 7 12 7C12.2761 7 12.5 7.22386 12.5 7.5Z"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</Link>
					<Link to="/demo/table">
						<svg
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
						>
							<title>Glob icon</title>
							<path
								d="M3.6001 9H20.4001M3.6001 15H20.4001M11.4999 3C9.81525 5.69961 8.92212 8.81787 8.92212 12C8.92212 15.1821 9.81525 18.3004 11.4999 21M12.5 3C14.1847 5.69961 15.0778 8.81787 15.0778 12C15.0778 15.1821 14.1847 18.3004 12.5 21M3 12C3 13.1819 3.23279 14.3522 3.68508 15.4442C4.13738 16.5361 4.80031 17.5282 5.63604 18.364C6.47177 19.1997 7.46392 19.8626 8.55585 20.3149C9.64778 20.7672 10.8181 21 12 21C13.1819 21 14.3522 20.7672 15.4442 20.3149C16.5361 19.8626 17.5282 19.1997 18.364 18.364C19.1997 17.5282 19.8626 16.5361 20.3149 15.4442C20.7672 14.3522 21 13.1819 21 12C21 9.61305 20.0518 7.32387 18.364 5.63604C16.6761 3.94821 14.3869 3 12 3C9.61305 3 7.32387 3.94821 5.63604 5.63604C3.94821 7.32387 3 9.61305 3 12Z"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</Link>
					<Link to="/demo/table">
						<svg
							width="24"
							height="24"
							viewBox="0 0 24 24"
							fill="none"
							xmlns="http://www.w3.org/2000/svg"
						>
							<title>Help bubble</title>
							<path
								d="M12 16V16.01M12 13C12.4498 13.0014 12.8868 12.8511 13.2407 12.5734C13.5945 12.2958 13.8444 11.907 13.95 11.4698C14.0557 11.0327 14.0109 10.5726 13.8229 10.1641C13.6349 9.75549 13.3147 9.42219 12.914 9.21801C12.5162 9.01422 12.0611 8.95103 11.6228 9.03873C11.1845 9.12642 10.7888 9.35984 10.5 9.70101M3 12C3 13.1819 3.23279 14.3522 3.68508 15.4442C4.13738 16.5361 4.80031 17.5282 5.63604 18.364C6.47177 19.1997 7.46392 19.8626 8.55585 20.3149C9.64778 20.7672 10.8181 21 12 21C13.1819 21 14.3522 20.7672 15.4442 20.3149C16.5361 19.8626 17.5282 19.1997 18.364 18.364C19.1997 17.5282 19.8626 16.5361 20.3149 15.4442C20.7672 14.3522 21 13.1819 21 12C21 9.61305 20.0518 7.32387 18.364 5.63604C16.6761 3.94821 14.3869 3 12 3C9.61305 3 7.32387 3.94821 5.63604 5.63604C3.94821 7.32387 3 9.61305 3 12Z"
								stroke="currentColor"
								stroke-width="2"
								stroke-linecap="round"
								stroke-linejoin="round"
							/>
						</svg>
					</Link>
				</div>
			</nav>
		</div>
	);
}
