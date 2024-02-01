from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
from express_vpn_wrapper import connect

class ExpressVPNInput(BaseModel):
    country_name: str = Field(..., description="Country's VPN to be used")


class ExpressVPNTool(BaseTool):
    """
    Express VPN Tool
    """
    name: str = "Express VPN Tool"
    args_schema: Type[BaseModel] = ExpressVPNInput
    description: str = "Use a Country's VPN"

    def _execute(self, country_name: str = None):
        try:
            connect(country_name)
            return { "connected": True }
        except Exception as e:
            print(e, "Error in connecting vpn")
            return { "connected": False }


if __name__ == '__main__':
    expressvpntool = ExpressVPNTool()