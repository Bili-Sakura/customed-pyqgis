import os
from typing import Dict, Literal, List
import time
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.pydantic_v1 import BaseModel, Field
import openai

load_dotenv(override=True)


class ParserDemo(BaseModel):
    # flag: bool = Field(
    #     description="Judge whether the table data is related to whole rock major elements"
    # )
    SAMPLE_NAME: str = Field(description="A list of Sample Name")
    SiO2: str = Field(description="A list of value of SiO2(WT%)")
    TiO2: str = Field(description="A list of value of TiO2(WT%)")
    ZrO2: str = Field(description="A list of value of ZrO2(WT%)")
    Al2O3: str = Field(description="A list of value of Al2O3(WT%)")
    Cr2O3: str = Field(description="A list of value of Cr2O3(WT%)")
    V2O3: str = Field(description="A list of value of V2O3(WT%)")
    V2O5: str = Field(description="A list of value of V2O5(WT%)")
    FE2O3T: str = Field(description="A list of value of FE2O3T(WT%)")
    FE2O3: str = Field(description="A list of value of FE2O3(WT%)")
    FEOT: str = Field(description="A list of value of FEOT(WT%)")
    FEO: str = Field(description="A list of value of FEO(WT%)")
    FECO3: str = Field(description="A list of value of FECO3(WT%)")
    CAO: str = Field(description="A list of value of CAO(WT%)")
    MGO: str = Field(description="A list of value of MgO(WT%)")
    MGCO3: str = Field(description="A list of value of MGCO3(WT%)")
    MNO: str = Field(description="A list of value of MnO(WT%)")
    K2O: str = Field(description="A list of value of K2O(WT%)")
    NA2O: str = Field(description="A list of value of NA2O(WT%)")
    P2O5: str = Field(description="A list of value of P2O5(WT%)")


class LLM:
    """
    代表一个大型语言模型(LLM)的类，可用于生成回答、表格判断或进行搜索。

    Attributes:
        model (str): 使用的LLM模型。
        temperature (float): 生成回答时使用的温度。
        base_url (str): OpenAI API的基础URL。
    """

    usage: Literal["DEMO", "UNKNOWN"] = (
        "DEMO"  # Define usage as a class attribute with Literal type
    )

    def __init__(
        self,
        model: str = "gpt-4-0613",
        temperature: float = 0,
        base_url: str = None,
    ):

        self.model = model
        self.temperature = temperature
        self.base_url = base_url or os.getenv("OPENAI_BASE_URL")

        self.init_llm()
        self.init_prompt()
        self.init_customed_llm()

    def init_llm(self) -> ChatOpenAI:
        """初始化LLM实例。"""
        self.llm = ChatOpenAI(
            model=self.model,
            temperature=self.temperature,
            base_url=self.base_url,
        )

    def init_prompt(self):
        """
        Initialize the prompt template based on the specified usage.

        @param usage: str
            Specifies the mode of usage
        """
        if self.usage == "DEMO":
            parser = JsonOutputParser(pydantic_object=ParserDemo)
            prompt_template = """
            You are a helpful geological assistant.
            You are going to extract data from a table data in html format.
            The output contains several elements like SIO2(WT%),TIO2(WT%) etc.
            For each variable, you need set a list of float value with the number the same as rock samples.
            For example:
            SAMPLE_NAME:["ROCK1","ROCK2","ROCK3"]
            SiO2:[0.12,0.14,0.74]

                quesution:{question}
                -----
                format_instructions:{format_instructions}
                """
            prompt = PromptTemplate(
                template=prompt_template,
                input_variables=[
                    "question",
                ],
                partial_variables={
                    "format_instructions": parser.get_format_instructions()
                },
            )
            self.parser = parser
            self.prompt = prompt
        else:
            pass

    def init_customed_llm(self):
        """

        @param self: The LLM instance.
        @raises ValueError: If any component (prompt, llm, or parser) is missing.
        """
        if self.prompt is None or self.llm is None or self.parser is None:
            raise ValueError("One or more components in the chain are None.")
        self.customed_llm = self.prompt | self.llm | self.parser

    def get_answer_dict(
        self,
        query: Dict,
    ) -> Dict:
        """
        For 'DEMO' usage:
        - Input query should contain:
            - 'question' (str): The question to be answered.

        - Output response will contain:
            - 'answer' (str): The generated answer.
        """
        self.__init__()

        retry = 0
        while retry < 3:
            try:
                # print("query:", query)
                llm_response = self.customed_llm.invoke(query)

                print("response:", llm_response)

                if self.is_correct_format(llm_response):
                    return llm_response
                else:
                    retry += 1
                    print("Unknown Response")
            except openai.APIStatusError as error:
                retry += 1
                print(
                    f"Error processing chunk. Retrying... Attempt {retry}; Error: {error}"
                )
                time.sleep(1)

        failed_answer = {
            field_name: "Unknown Response"
            for field_name in set(self.parser.pydantic_object.__fields__.keys())
        }
        return failed_answer

    def is_correct_format(self, response: Dict) -> bool:
        """
        Check if the response is in the correct format.

        @param response: Dict
            The response to be checked.

        @return bool
            True if the response is in the correct format, False otherwise.
        """
        if not isinstance(response, dict):
            return False

        model_fields = set(self.parser.pydantic_object.__fields__.keys())
        return set(response.keys()) == model_fields and len(response) == len(
            model_fields
        )
