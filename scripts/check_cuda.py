import torch

def main():
    print("torch:", torch.__version__)
    print("torch cuda:", torch.version.cuda)
    print("cuda available:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("device count:", torch.cuda.device_count())
        print("device name:", torch.cuda.get_device_name(0))
        x = torch.randn(1024, 1024, device="cuda")
        y = x @ x
        print("gpu test:", y.mean().item())
    else:
        print("CUDA is not available. Check PyTorch installation and NVIDIA driver.")

if __name__ == "__main__":
    main()