import { useEffect, useRef, useState } from "react";

export default function DistrictSelector() {
	const [open, setOpen] = useState(false);
	const dropdownRef = useRef<HTMLDivElement>(null);

	useEffect(() => {
		function handleClickOutside(event: MouseEvent) {
			if (
				dropdownRef.current &&
				!dropdownRef.current.contains(event.target as Node)
			) {
				setOpen(false);
			}
		}

		if (open) {
			document.addEventListener("mousedown", handleClickOutside);
		} else {
			document.removeEventListener("mousedown", handleClickOutside);
		}
		return () => {
			document.removeEventListener("mousedown", handleClickOutside);
		};
	}, [open]);

	return (
		<div className="relative flex items-center" ref={dropdownRef}>
			<svg
				width="24"
				height="24"
				viewBox="0 0 24 24"
				fill="none"
				xmlns="http://www.w3.org/2000/svg"
			>
				<title>Circle seperator icon</title>
				<path
					fillRule="evenodd"
					clipRule="evenodd"
					d="M11.5 16C12.6935 16 13.8381 15.5259 14.682 14.682C15.5259 13.8381 16 12.6935 16 11.5C16 10.3065 15.5259 9.16193 14.682 8.31802C13.8381 7.47411 12.6935 7 11.5 7C10.3065 7 9.16193 7.47411 8.31802 8.31802C7.47411 9.16193 7 10.3065 7 11.5C7 12.6935 7.47411 13.8381 8.31802 14.682C9.16193 15.5259 10.3065 16 11.5 16Z"
					fill="#003049"
				/>
			</svg>
			<button
				type="button"
				className="text-[#013148] gap-2 items-center pl-3 py-4 font-bold flex cursor-pointer"
				onClick={() => setOpen((v) => !v)}
				aria-haspopup="listbox"
				aria-expanded={open}
			>
				Northstop Unified School District
				<svg
					width="16"
					height="16"
					viewBox="0 0 16 16"
					fill="none"
					xmlns="http://www.w3.org/2000/svg"
				>
					<title>School district selector dropdown indicattor</title>
					<path
						d="M4 6L8 10L12 6"
						stroke="#003049"
						strokeWidth="2"
						strokeLinecap="round"
						strokeLinejoin="round"
					/>
				</svg>
			</button>
			{open && (
				<select
					className="block appearance-none w-full bg-white border border-gray-200 text-gray-700 py-2 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
					aria-label="District selector"
				>
					<optgroup label="Recent">
						<option value="northstop">Northstop Unified School District</option>
						<option value="another">Another District</option>
					</optgroup>
				</select>
			)}
		</div>
	);
}
