# api/routes.py

from fastapi import APIRouter
from pydantic import BaseModel
from orchestrator.planner import plan
from executor.executor import dry_run, execute

ask_router = APIRouter()

class AskRequest(BaseModel):
    prompt: str

class ExecuteRequest(BaseModel):
    steps: list[str]


@ask_router.post("/")
async def handle_prompt(request: AskRequest):
    steps = plan(request.prompt)
    dry_run_output = []

    for step in steps:
        dry_run(step)
        dry_run_output.append(step)
        # In future: confirm or auto-execute based on permission flag

    return {
        "message": "Planned",
        "prompt": request.prompt,
        "steps": dry_run_output
    }



@ask_router.post("/execute")
async def confirm_and_execute(request: ExecuteRequest):
    executed = []
    for cmd in request.steps:
        try:
            execute(cmd)
            executed.append(cmd)
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Failed to execute: {cmd} | {str(e)}")

    return {"message": "Executed", "commands": executed}