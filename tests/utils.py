from strawberry_classes.mutations import Mutation

mutation = Mutation()

async def clear_tables() -> None:
	result = await mutation.truncate_table("author")
	assert result == "success"
	result = await mutation.truncate_table("post")
	assert result == "success"
	result = await mutation.truncate_table("postcomment")
	assert result == "success"
