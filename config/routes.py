
def register_routes(api, app, root="api"):
    from app.product import register_routes as attach_product

    # Add routes
    attach_product(api, app)
