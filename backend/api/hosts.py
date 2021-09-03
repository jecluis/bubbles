# Copyright (C) 2021 SUSE, LLC
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
from fastapi import APIRouter, Request
from bubbles.bubbles import Bubbles
#from bubbles.backend.controllers.hosts import 

router = APIRouter(prefix="/hosts", tags=["hosts"])


@router.get("/list")
async def get_list(request: Request):
    bubbles: Bubbles = request.app.state.bubbles
    assert bubbles.ctrls.hosts is not None
    return bubbles.ctrls.hosts.list()
