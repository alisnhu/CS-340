1. How do you write programs that are maintainable, readable, and adaptable? Especially consider your work on the CRUD Python module from Project One, which you used to connect the dashboard widgets to the database in Project Two. What were the advantages of working in this way? How else could you use this CRUD Python module in the future?

When developing the CRUD module, I applied important software engineering principles to write maintainable, readable, and adaptable programs. First, I designed the module according to the single responsibility principle - each method had a specific task and was responsible only for that task. For example, the create() method was only responsible for adding data, and the read() method was only responsible for reading data.

Working this way had many advantages:
- I avoided code repetition because database operations were managed from a central point
- Error handling was standardized and consistently implemented across all methods
- Security measures like schema control were collected in one place
- Testing and debugging the code became easier

I can easily use this CRUD module in different projects in the future. For example:
- I can integrate it into different MongoDB projects with minimal changes
- I can develop it by adding new features (e.g., connection pool)
- I can adapt it to different data schemas
- I can turn it into a library that other developers can use

2. How do you approach a problem as a computer scientist? Consider how you approached the database or dashboard requirements that Grazioso Salvare requested. How did your approach to this project differ from previous assignments in other courses? What techniques or strategies would you use in the future to create databases to meet other client requests?

I took a systematic approach for the Grazioso Salvare project. As a first step, I analyzed the client's needs in detail. I identified basic requirements such as categorizing rescue dogs, displaying location information, and filtering features.

This project was different from assignments in other courses because:
- I was working to meet the needs of a real client
- I needed to develop a complex database structure and user interface
- I needed to consider practical issues like performance and usability

Strategies I would use in similar projects in the future:
- Detailed analysis of customer requirements
- Design of a modular and extensible architecture
- Planning security and data integrity controls from the start
- Comprehensive testing and error management strategies
- Iterative development based on user feedback

3. What do computer scientists do, and why does it matter? How would your work on this type of project help a company, like Grazioso Salvare, to do their work better?

Computer scientists bridge the gap between technology and business needs. In this project, I developed a system that helps Grazioso Salvare manage rescue dogs more effectively.

Benefits my project provided to the company:
- Central and organized data management
- Quick data analysis through visual dashboard
- Effective dog selection with location-based search and filtering features
- Automation and acceleration of business processes

Such projects add value to companies because:
- They automate manual processes and reduce errors
- They facilitate data-based decision making
- They increase operational efficiency
- They make employees' work easier through user-friendly interfaces

In conclusion, as a computer scientist, the solutions I develop help companies work more efficiently and reach their goals faster.
