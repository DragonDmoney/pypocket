from typing import Optional
import requests
from ..models import (
    Application,
    Node,
    QueryAddressHeight,
    QueryAppsResponse,
    QueryNodesResponse,
    ValidatorOpts,
    ApplicationOpts,
    QuerySigningInfoResponse,
    QueryPaginatedHeightAndAddrParams,
    QueryHeightAndApplicationsOpts,
    QueryHeightAndValidatorOpts,
    StakingStatus,
    JailedStatus,
)
from ..utils import make_api_url, post


def get_app(
    provider_url: str,
    address: str,
    height: int = 0,
    session: Optional[requests.Session] = None,
) -> Application:
    request = QueryAddressHeight(height=height, address=address)
    route = make_api_url(provider_url, "/query/app")
    resp_data = post(route, session, **request.dict())
    return Application(**resp_data)


def get_apps(
    provider_url: str,
    height: int = 0,
    page: int = 0,
    per_page: int = 100,
    staking_status: str = "",
    blockchain: str = "",
    session: Optional[requests.Session] = None,
) -> QueryAppsResponse:
    if staking_status:
        staking_status = getattr(StakingStatus, staking_status, "")
    opts = ApplicationOpts(
        page=page,
        per_page=per_page,
        staking_status=staking_status,
        blockchain=blockchain,
    )
    request = QueryHeightAndApplicationsOpts(height=height, opts=opts)
    route = make_api_url(provider_url, "/query/apps")
    resp_data = post(route, session, **request.dict())
    return QueryAppsResponse(**resp_data)


def get_node(
    provider_url: str,
    address: str,
    height: int = 0,
    session: Optional[requests.Session] = None,
) -> Node:
    request = QueryAddressHeight(height=height, address=address)
    route = make_api_url(provider_url, "/query/node")
    resp_data = post(route, session, **request.dict())
    return Node(**resp_data)


def get_nodes(
    provider_url: str,
    height: int = 0,
    page: int = 0,
    per_page: int = 100,
    staking_status: str = "",
    jailed_status: str = "",
    blockchain: str = "",
    session: Optional[requests.Session] = None,
) -> QueryNodesResponse:
    if staking_status:
        staking_status = getattr(StakingStatus, staking_status, "")
    if jailed_status:
        jailed_status = getattr(JailedStatus, jailed_status, "")
    opts = ValidatorOpts(
        page=page,
        per_page=per_page,
        staking_status=staking_status,
        jailed_status=jailed_status,
        blockchain=blockchain,
    )
    request = QueryHeightAndValidatorOpts(height=height, opts=opts)
    route = make_api_url(provider_url, "/query/nodes")
    resp_data = post(route, session, **request.dict())
    return QueryNodesResponse(**resp_data)


def get_signing_info(
    provider_url: str,
    height: int = 0,
    address: Optional[str] = None,
    page: int = 0,
    per_page: int = 100,
    session: Optional[requests.Session] = None,
) -> QuerySigningInfoResponse:
    request = QueryPaginatedHeightAndAddrParams(
        height=height, address=address, page=page, per_page=per_page
    )
    route = make_api_url(provider_url, "/query/signinginfo")
    resp_data = post(route, session, **request.dict())
    return QuerySigningInfoResponse(**resp_data)