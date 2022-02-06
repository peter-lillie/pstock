import typing as tp

import httpx

from pstock.schemas.trend import Trends

from .quote import get_yf_quote_summary_content_async, get_yf_quote_summary_content_sync


async def get_trends_async(
    symbol: str, client: tp.Optional[httpx.AsyncClient] = None
) -> Trends:
    """Get [Trends][pstock.schemas.Trends] data from yahoo-finance.

    [Trends][pstock.schemas.Trends] are parsed from the `quote_summary` generated by
    [get_quote_summary][pstock.yahoo_finance.get_quote_summary].

    Is provided symbol has no Trends (crypto/ETF): an empty
    [Trends][pstock.schemas.Trends] object is returned.

    Args:
        symbol (str): A stock symbol availlable in yahoo-finance
        client (tp.Optional[httpx.AsyncClient], optional): Defaults to None.

    Returns:
        [pstock.schemas.Trends][]
    """
    content = await get_yf_quote_summary_content_async(symbol, client=client)
    return Trends.from_yf(content=content)


def get_trends_sync(symbol: str, client: tp.Optional[httpx.Client] = None) -> Trends:
    """Get [Trends][pstock.schemas.Trends] data from yahoo-finance.

    [Trends][pstock.schemas.Trends] are parsed from the `quote_summary` generated by
    [get_quote_summary][pstock.yahoo_finance.get_quote_summary].

    Is provided symbol has no Trends (crypto/ETF): an empty
    [Trends][pstock.schemas.Trends] object is returned.

    Args:
        symbol (str): A stock symbol availlable in yahoo-finance
        client (tp.Optional[httpx.Client], optional): Defaults to None.

    Returns:
        [pstock.schemas.Trends][]
    """
    content = get_yf_quote_summary_content_sync(symbol, client=client)
    return Trends.from_yf(content=content)
