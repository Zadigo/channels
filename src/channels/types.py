from collections.abc import Awaitable, Callable
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    from channels.consumer import AsyncConsumer, SyncConsumer
    from channels.layers import BaseChannelLayer


type TypeChannelLayer = BaseChannelLayer

type TypeAsyncFunction[T = Any] = Callable[[T], Awaitable[Any]]

type TypeHandlerFunction[T = Any] = Callable[[T], Any]

type TypeConsumer = AsyncConsumer | SyncConsumer
