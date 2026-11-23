def first_call(llm, question, system, max_tokens=100):
    """Ask one question. Return the text, the stop reason and the token counts."""
    payload = [{
        "content": question,
        "role": "user"
    }]
    resp_obj = llm.messages.create(system=system, messages=payload, max_tokens=max_tokens)

    result = {
        "text": resp_obj.text,
        "stop_reason": resp_obj.stop_reason,
        "input_tokens": resp_obj.usage.input_tokens,
        "output_tokens": resp_obj.usage.output_tokens,
    }
    # print (result)
    return result
