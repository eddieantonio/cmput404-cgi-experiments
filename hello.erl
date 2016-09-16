#!/usr/bin/env escript
-module(hello).

-export([main/1]).

main(_) ->
    print(),
    print("Hello, from Erlang!").

print() -> print("").
print(String) ->
    io:format("~s~n", [String]).
