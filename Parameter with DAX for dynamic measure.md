# Parameter with DAX for dynamic measure

## Requirements
* Power BI file saved as .pbip
* Tabular Editor

## Case 01: Parameter for Dynamic Measure
### 1. Create extended property of the "Parameter Fields" column:
1. Click "Add" to create a new member.
2. Set up properties:
	* Name: `ParameterMetadata`
	* Type: `Json`
	* Value: `("version":3,"kind:2"}`

### 2. "Parameter Value" column needs to be grouped by "Parameter Fields":
1. Properties > Options > Group by Columns
2. Click "add" and select "Parameter Fields"

### 3. Sample Dax Code
```
EVALUATE
SELECTCOLUMNS (
	{
		("Total Sales", NAMEOF ([Total Sales]), 0),
		("Total Profit", NAMEOF ([Total Profit]) , 1)
	},
	"Parameter Values", [Value1],
	"Parameter Fields", [Value2],
	"Parameter Index", [Value3]
)
```

## Case 02: Parameter for Dynamic Measure with Hierarchy
### 1. Sample Dax Code
```
SELECTCOLUMNS (
	{
		("Sales", "Total Sales", NAMEOF([Total Sales]), 0),
		("Sales", "Total Gross Sales", NAMEOF([Total Gross Sales]), 1), 
		("Sales", "Total Profit", NAMEOF([Total Profit]), 2),
		("Units", "Total Units Sold", NAMEOF( [Total Units Sold]), 3)
	},
	"Parameter Values Lvl 1", [Value1],
	"Parameter Values", [Value2],
	"Parameter Fields", [Value3],
	"Parameter Index", [Value4]
)
```

## Reference article
* ![Fields Parameters in Power BI - Accessed: Oct/2024](https://www.sqlbi.com/articles/fields-parameters-in-power-bi/)
