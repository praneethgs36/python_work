def print_models(unprinted_designs, completed_models):
    """Simulated 3d-printing designs and moving them to another list. """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f"Printing {current_design}...")
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """Show models that are printed. """
    print("The following models are completed: ")
    for model in completed_models:
        print(model)