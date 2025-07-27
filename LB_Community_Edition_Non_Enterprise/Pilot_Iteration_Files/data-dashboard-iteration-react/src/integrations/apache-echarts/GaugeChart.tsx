import * as echarts from "echarts";
import type React from "react";
import { useEffect, useRef } from "react";
import "./gauge-chart.css";

const option = {
	series: [
		{
			type: "gauge",
			startAngle: 180,
			endAngle: 0,
			center: ["50%", "75%"],
			radius: "90%",
			min: 0,
			max: 1,
			splitNumber: 8,
			axisLine: {
				lineStyle: {
					width: 6,
					color: [
						[0.25, "#FF6E76"],
						[0.5, "#FDDD60"],
						[0.75, "#58D9F9"],
						[1, "#7CFFB2"],
					],
				},
			},
			pointer: {
				icon: "path://M12.8,0.7l12,40.1H0.7L12.8,0.7z",
				length: "12%",
				width: 20,
				offsetCenter: [0, "-60%"],
				itemStyle: {
					color: "auto",
				},
			},
			axisTick: {
				length: 12,
				lineStyle: {
					color: "auto",
					width: 2,
				},
			},
			splitLine: null,
			axisLabel: {
				color: "#464646",
				fontSize: 20,
				distance: -60,
				rotate: "tangential",
				formatter: (value: number) => {
					if (value === 0.875) {
						return "Grade A";
					} else if (value === 0.625) {
						return "Grade B";
					} else if (value === 0.375) {
						return "Grade C";
					} else if (value === 0.125) {
						return "Grade D";
					}
					return "";
				},
			},
			title: {
				offsetCenter: [0, "-10%"],
				fontSize: 20,
			},
			detail: {
				fontSize: 30,
				offsetCenter: [0, "-35%"],
				valueAnimation: true,
				formatter: (value: number) => {
					if (value < 0.2) {
						return "Red";
					} else if (value < 0.4) {
						return "Orange";
					} else if (value < 0.6) {
						return "Yellow";
					} else if (value < 0.8) {
						return "Green";
					} else {
						return "Blue";
					}
				},
				color: "inherit",
			},
			data: [
				{
					value: 0.7,
					name: "Grade Rating",
				},
			],
		},
	],
};

const GaugeChart: React.FC = () => {
	const chartRef = useRef<HTMLDivElement>(null);
	const chartInstance = useRef<echarts.EChartsType | null>(null);

	useEffect(() => {
		if (chartRef.current) {
			chartInstance.current = echarts.init(chartRef.current);
			chartInstance.current.setOption(option);
		}
		return () => {
			chartInstance.current?.dispose();
		};
	}, []);

	return <div ref={chartRef} className="gauge-chart-container" />;
};

export default GaugeChart;
