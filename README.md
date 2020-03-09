# PE-Class
A concept system to filter through potential private equity investments to determine most appealing options. Focused primarily on software company investments.

The database of 10,000 start-ups was created first by randomizing Year 1,2, and 3 revenues for the fictitious companies. The first year revenue values range from 100,000 to 2,500,000. Second year range: 150,000 to 3,000,000. For the third year, to make things a bit simpler and certain, a 12% growth rate was applied to year 2 revenue.

Next, a randomized ratio of "Owner Equity" was created to represent founder equity held at the current date.

Total Assets and Liabilities were created next. Asset value was randomly selected from 1,000,000 to 10,000,000. Liabilities were picked from a range of 1,000,000 to 8,000,000. Current liabilities were selected by assuming a ratio of 25% of total liabilities. Current assets were calculated in the same way. 

Liquidity ratio was then calculated from the above information.

A randomized COGS to revenue average ratio was created between values of 0.1 and 0.8.

Lastly, a gross profit margin was created from revenue information and COGS


After this database was created, a simple filtering system was applied only allowing for the following investment criteria: Founder Equity: Greater than 50%, Year 1 Revenue<Year 2 Revenue<Year 3 Revenue, a Liquidity Ratio greater than or equal to 1 and an average COGS ratio of less than or equal to 30%.
