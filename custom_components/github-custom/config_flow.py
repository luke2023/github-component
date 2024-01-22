from homeassistant import config_entries

class MyCustomIntegrationConfigFlow(config_entries.ConfigFlow, domain="my_custom_integration"):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            # Store the device name in the options and create the entry
            return self.async_create_entry(title=user_input["name"], data=user_input)

        # Render the form for the user to input the device name
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({"name": str}),
        )
