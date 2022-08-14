class RequestUserMixin:

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.setdefault('user', self.request.user)

        return context
