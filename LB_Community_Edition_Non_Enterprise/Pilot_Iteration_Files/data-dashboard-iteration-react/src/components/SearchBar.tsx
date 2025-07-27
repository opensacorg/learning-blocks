import { useForm } from "@tanstack/react-form";
import * as React from "react";
import "./SearchBar.css";

// Example preview data
const previewResults = [
	{
		category: "Users",
		items: [
			{ id: 1, label: "Alice" },
			{ id: 2, label: "Bob" },
		],
	},
	{
		category: "Projects",
		items: [
			{ id: 3, label: "Apollo" },
			{ id: 4, label: "Gemini" },
		],
	},
];

export default function SearchBar({ className }: { className?: string }) {
	const [showDropdown, setShowDropdown] = React.useState(false);
	const [query, setQuery] = React.useState("");

	const form = useForm({
		defaultValues: { search: "" },
		onSubmit: ({ value }) => {
			// handle search submit
			setQuery(value.search);
			setShowDropdown(true);
		},
	});

	// Filter preview results by query
	const filteredResults = React.useMemo(() => {
		if (!query) return previewResults;
		return previewResults
			.map((cat) => ({
				...cat,
				items: cat.items.filter((item) =>
					item.label.toLowerCase().includes(query.toLowerCase()),
				),
			}))
			.filter((cat) => cat.items.length > 0);
	}, [query]);

	return (
		<div className={`searchbar-root ${className}`}>
			<form
				onSubmit={form.handleSubmit}
				autoComplete="off"
				className="searchbar-form"
			>
				<input
					name="search"
					value={form.state.values.search}
					onChange={(e) => {
						form.setFieldValue("search", e.target.value);
						setQuery(e.target.value);
						setShowDropdown(true);
					}}
					onFocus={() => {
						setShowDropdown(true);
					}}
					onBlur={() => setTimeout(() => setShowDropdown(false), 150)}
					placeholder="Search..."
					className="searchbar-input"
				/>
			</form>
			{showDropdown && filteredResults.length > 0 && (
				<div className="searchbar-dropdown">
					{filteredResults.map((cat) => (
						<div key={cat.category} className="searchbar-category-block">
							<div className="searchbar-category-heading">{cat.category}</div>
							{cat.items.map((item) => (
								<button
									key={item.id}
									type="button"
									className="searchbar-result-item"
									onMouseDown={(e) => e.preventDefault()}
									onClick={() => {
										form.setFieldValue("search", item.label);
										setShowDropdown(false);
									}}
								>
									{item.label}
								</button>
							))}
						</div>
					))}
				</div>
			)}
		</div>
	);
}
