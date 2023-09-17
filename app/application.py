import os.path
from croydon.baseapp import BaseApp


class Application(BaseApp):

    def __init__(self):
        app_dir = os.path.abspath(os.path.dirname(__file__))
        project_dir = os.path.abspath(os.path.join(app_dir, ".."))
        super().__init__(project_dir=project_dir)

    def setup_routes(self) -> None:
        from .controllers.api.v1.simwatch import simwatch_ctrl
        from .controllers.api.v1.airports import airports_ctrl
        from .controllers.api.v1.pilots import pilots_ctrl
        self.include_router(simwatch_ctrl)
        self.include_router(airports_ctrl)
        self.include_router(pilots_ctrl)
