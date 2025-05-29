from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, FileWriterTool

@CrewBase
class Demoproject2:
    """Reportgencrew crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def financial_data_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['financial_data_researcher'],
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @agent
    def news_data_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['news_data_researcher'],
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @agent
    def social_media_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['social_media_researcher'],
            verbose=True,
            tools=[SerperDevTool(), ScrapeWebsiteTool()]
        )

    @agent
    def validity_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config['validity_analyst'],
            verbose=True,
            tools=[SerperDevTool()]
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config['report_writer'],
            verbose=True,
            tools=[FileWriterTool()]
        )

    @task
    def financial_data_researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['financial_data_researcher_task']
        )

    @task
    def news_data_researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['news_data_researcher_task']
        )

    @task
    def social_media_researcher_task(self) -> Task:
        return Task(
            config=self.tasks_config['social_media_researcher_task']
        )

    @task
    def validity_analyst_task(self) -> Task:
        return Task(
            config=self.tasks_config['validity_analyst_task']
        )

    @task
    def report_writer_task(self) -> Task:
        return Task(
            config=self.tasks_config['report_writer_task'],
            output_file='LASTGERNERATEDREPORT.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Reportgencrew crew"""
        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
