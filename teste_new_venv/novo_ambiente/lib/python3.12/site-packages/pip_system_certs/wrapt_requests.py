import ssl

_injected = False

def inject_truststore():
    global _injected
    if not _injected:
        try:
            # Try to use pip's vendored truststore first (available in pip 24.2+)
            try:
                from pip._vendor import truststore
            except ImportError:
                # Fallback to standalone truststore for older pip versions
                try:
                    import truststore
                except ImportError:
                    print("pip_system_certs: ERROR: truststore not available")
                    return
            
            # Check if truststore is already injected globally
            default_context = ssl.create_default_context()
            if isinstance(default_context, truststore.SSLContext):
                _injected = True
                return
            
            # Inject truststore for all SSL connections (pip, requests, etc.)
            truststore.inject_into_ssl()
            _injected = True
        except Exception as ex:
            print("pip_system_certs: ERROR: could not inject truststore:", ex)
